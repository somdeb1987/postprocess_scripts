import numpy as np
import os
import subprocess as sp
#===============================================================================
def read_column_with_vname(fname,v_name):
#read a specific column with a value for a certain header
    vnames  = read_header_values(fname)
    n_items = get_max_lines(fname)
    col_values = np.zeros(n_items)
    f = open(fname, 'r')
    for i, line in enumerate(f):
        l_values = line.split()
        if i > 0 :
            col_values[i-1] = float(l_values[vnames.index(v_name)])
    f.close()
    return col_values
#===============================================================================
def read_line_with_value_for_vname(fname,v_name,v_value):
#read a specific line with a value for a certain variable
#n_ele    = element number (line_value-1)
#n_line   = line number
#val_line = line values 
    vnames = read_header_values(fname)
    val_line = None
    n_line = None
    n_ele  = None
    f = open(fname, 'r')
    for i, line in enumerate(f):
        v_values = line.split()
        if i > 0 and float(v_values[vnames.index(v_name)]) == v_value :
            val_line = v_values
            n_line = i + 1
            n_ele =i
            break
    f.close()
    return n_ele, n_line, val_line
#===============================================================================
def read_header_values(fname):
#read the header names of the file
    f = open(fname, 'r')
    for i, line in enumerate(f):
        if i == 0:
            vnames = line.split()
        elif i > 0:
            break
    # Close the file.
    f.close()
    # Return values.
    return(vnames)
#===============================================================================
def get_max_lines(fname):
#get max number of lines of the file
    my_command = "sed -n '$=' " + fname
    n_maxline=int(sp.getoutput(my_command))
    return(n_maxline)
#===============================================================================

