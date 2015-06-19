from meep_mpi import *  # make it 'meep_mpi' for MPI-meep and 'meep' for non-MPI meep

grid_size_x = 16.0
grid_size_y = 32.0
grid_size_z = 0.5+0.38

class epsilon(PolygonCallback3D):
    def __init__(self):
        PolygonCallback3D.__init__(self)
        master_printf("Callback function for epsilon contructed.\n")
        master_printf("Now defining the matrial stacks...\n")
        ms = numpy.zeros([4,4])
        #first material stack : 0.5 micron of SiOx (eps = 2.31), with 0.38 micron of air (eps = 1.0) on top
        ms[0] = [1, 0.5, 2.31, 2] #material stack ID, height of material, eps of material, number of lines in this stack
        ms[1] = [1, 0.38, 1.0, 2]
        #second material stack : 0.5 micron of SiOx (eps = 2.31), with 0.38 micron of Si (eps = 12.0) on top
        ms[2] = [2, 0.5, 2.31, 2]
        ms[3] = [2, 0.38, 12.0, 2]
        self.add_material_stacks_from_numpy_matrix(ms, 2)
        master_printf("Now defining the polygons...\n")
        wg_length = 16.0
        pad_size = 4.0
        wg_width = 1.5
        grid_size_y = 32.0
        #polygon 1 : area with material stack 1 (SiOx and air)
        pol1_points = numpy.zeros((5,2))
        pol1_points[0] = [0.0,0.0]
        pol1_points[1] = [wg_length, 0.0]
        pol1_points[2] = [wg_length, pad_size]
        pol1_points[3] = [0.0, pad_size]
        pol1_points[4] = [0.0, 0.0]
        self.add_polygon(pol1_points, 1)
        #polygon 2 : area with material stack 2 (SiOx and Si)
        pol2_points = numpy.zeros((5,2))
        pol2_points[0] = [0.0, pad_size]
        pol2_points[1] = [wg_length, pad_size]
        pol2_points[2] = [wg_length, pad_size+wg_width]
        pol2_points[3] = [0.0, pad_size+wg_width]
        pol2_points[4] = [0.0, pad_size]
        self.add_polygon(pol2_points, 2)
        #polygon 3 : area with material stack 1 (SiOx and air)
        pol3_points = numpy.zeros((5,2))
        pol3_points[0] = [0.0,pad_size+wg_width]
        pol3_points[1] = [wg_length, pad_size+wg_width]
        pol3_points[2] = [wg_length, grid_size_y]
        pol3_points[3] = [0.0, grid_size_y]
        pol3_points[4] = [0.0,pad_size+wg_width]
        self.add_polygon(pol3_points, 1)
        master_printf("Polygons OK....\n")

comp_vol = vol3d(grid_size_x,grid_size_y,grid_size_z,10.0)
material = epsilon()
set_EPS_Callback(material.__disown__())
use_averaging(False)
s = structure(comp_vol, EPS, pml(0.25))
f = fields(s)
eps_file =  prepareHDF5File("3d_waveguide.h5")
f.output_hdf5(Dielectric, comp_vol.surroundings(), eps_file)
