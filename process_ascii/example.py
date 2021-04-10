import ascii_utilities as ascu

work_dir="/home/somdeb/works/aiaa/mhd/sadhana_2021/exec/2d_hd_IsentropicVortex/tvd"
file_dir="solution_statistics_nc=4_l=7"
file_name = "error_l1_norm_global_01.dat"

path_name= work_dir + '/' + file_dir + '/' + file_name
vnames                           = ascu.read_header_values(path_name)
p                                = ascu.get_max_lines(path_name)
[ele_number, l_number, l_values] = ascu.read_line_with_value_for_vname(path_name,"time",10.)
data                             = ascu.read_column_with_vname(path_name,"time")

print("maxlines =",p)
print("vnames =",vnames)
print("dens index", vnames.index("dens"))
print("ele_number =", ele_number)
print("l_number =", l_number)
print("l_values =", l_values)
print("data =", data[1:10])

