#include <python.h>

/**
 * print_python_list_info - function to print basic info about Python lists
 * @p: input pointer to PyObject or the Python list to print info about
 */

void print_python_list_info(PyObject *p)
{
	size_t len = PyList_size(p);

	printf("[*] Size of the Python list = %d\n", len);
	printf("[*] Allocated = %d\n", object->allocated);
	for (i = 0, i < len, i++)
		print("Element %d: %\n", i, "str");
}
