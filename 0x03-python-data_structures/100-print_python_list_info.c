#include <Python.h>

/**
 * print_python_list_info - prints python list info
 * @p: python object
 **/

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = PyList_Size(p), i;
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;
    PyObject *item;
    const char *type_name;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", allocated);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);
        type_name = Py_TYPE(item)->tp_name;

        printf("Element %zd: %s\n", i, type_name);
    }
}

