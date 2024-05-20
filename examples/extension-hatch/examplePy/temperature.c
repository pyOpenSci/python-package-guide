#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *
temperature_celsius_to_fahrenheit(PyObject *self, PyObject *args)
{
    long celsius;
    PyObject *ret;

    if (!PyArg_ParseTuple(args, "l", celsius))
        return NULL;

    celsius = (celsius * 9/5) + 32;

    ret = PyLong_FromLong(celsius);
    Py_INCREF(ret);
    return ret;
}

static PyObject *
temperature_fahrenheit_to_celsius(PyObject *self, PyObject *args)
{
    long fahrenheit;
    PyObject *ret;

    if (!PyArg_ParseTuple(args, "l", fahrenheit))
        return NULL;

    fahrenheit = (fahrenheit - 32) * 9/5;

    ret = PyLong_FromLong(fahrenheit);
    Py_INCREF(ret);
    return ret;
}

static PyMethodDef CoreMethods[] = {
    {"celsius_to_fahrenheit",  temperature_celsius_to_fahrenheit, METH_VARARGS, "Convert temperature from Celsius to Fahrenheit"},
    {"fahrenheit_to_celsius",  temperature_fahrenheit_to_celsius, METH_VARARGS, "Convert temperature from Fahrenheit to Celsius"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef temperaturemodule = {
    PyModuleDef_HEAD_INIT,
    "temperature",   /* name of module */
    NULL,     /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    CoreMethods
};

PyMODINIT_FUNC
PyInit_temperature(void)
{
    PyObject *m;

    m = PyModule_Create(&temperaturemodule);
    if (m == NULL)
        return NULL;

    return m;
}
