#include <Python.h>

/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: input pointer to PyObject or the Python list to print info about
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t len, allocated, i;
	PyObject *item;

	list = (PyListObject *)p;
	len = PyList_size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python list = %ld\n", len);
	printf("[*] Allocated = %ld\n", allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
