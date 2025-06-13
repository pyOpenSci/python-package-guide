from babel.messages import pofile

from pathlib import Path
from babel.messages import pofile

# Paths needed for this script
BASE_DIR = Path(__file__).resolve().parent.parent  # Repository base directory
LOCALES_DIR = BASE_DIR / "locales"  # Locales directory
STATIC_DIR = BASE_DIR / "_static"  # Static directory

def calculate_translation_percentage(po_path : Path, locale : str) -> dict:
    """
    Calculate the translation percentage for a given .po file.

    Parameters
    ----------
    po_path : Path
        Path to the .po file.
    locale : str
        Locale code (e.g., 'es', 'fr').

    Returns
    -------
    dict
        A dictionary containing the total number of strings, translated strings,
        fuzzy strings, untranslated strings, and the translation percentage.
    """
    with open(po_path, "r", encoding="utf-8") as f:
        catalog = pofile.read_po(f, locale=locale)

    total = 0
    translated = 0
    fuzzy = 0

    for message in catalog:
        if message.id:
            total += 1
            # Check if the message is fuzzy
            # Fuzzy messages are not considered translated
            if message.fuzzy:
                fuzzy += 1
                break
            # Check if the message is translated
            if message.string:
                translated += 1

    percentage = (translated / total * 100) if total > 0 else 0

    return {
        "total": total,
        "translated": translated,
        "fuzzy": fuzzy,
        "untranslated": total - translated - fuzzy,
        "percentage": round(percentage, 2)
    }

def main():
    # Get all .po files in the locales directory
    po_files = list(LOCALES_DIR.rglob("*.po"))

    # Let's use a dictionary to store the results
    #
    # We will store the info as
    # {
    #    "es": {
    #        "file1": {
    #            "total": 100,
    #            "translated": 50,
    #            "fuzzy": 0,
    #            "untranslated": 50,
    #            "percentage": 50.0
    #        },
    #        ...
    #    },
    #    "fr": {
    #        "file1": {
    #            "total": 100,
    #            "translated": 50,
    #            "fuzzy": 0,
    #            "untranslated": 50,
    #            "percentage": 50.0
    #        },
    #        ...
    # }
    results = {}

    # Calculate translation percentages for each file
    for po_file in po_files:
        # Get the locale from the file path
        locale = po_file.parent.parent.name
        stats = calculate_translation_percentage(po_file, locale)
        print(f"({po_file.stem}): {stats['percentage']}% translated ({stats['translated']} of {stats['total']})")

        # Store the results in the dictionary
        if locale not in results:
            results[locale] = {}

        results[locale][po_file.stem] = stats

    # Dump the results to a JSON file
    with open(STATIC_DIR / "translation_stats.json", "w") as f:
        import json
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    main()
