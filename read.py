import MDAnalysis
import numpy

#Choose the trajectory of p atom
def read_traj(p,frame):
    shape = protein.residue[p].atoms.positions.shape
    residue = protein.residues[p].atoms.positions.reshape(1,shape[0]*shape[1])
    for i in range(1,frame):
        u.trajectory[i]
        r=protein.residues[p].atoms.positions.reshape(1,shape[0]*shape[1])
        residue=np.row_stack((residue,r))
    return residue
    
#The first parameter is *psf file; the second parameter is the trajectory file.
u = MDAnalysis.Universe("/home/wangbing/dhd/4k3b_popcwi.psf",
                        "/home/wangbing/dhd/4k3b_popcwi_eq.dcd")
#select protein
protein = u.select_atoms("protein")
frame = len(u.trajectory)
residue_num = len(protein.residues)

for i in range(residue_num):
    residue = read_traj(i,frame)
    #set filename
    filename = 'residue'+str(i)+
    npsave(filename,residue)
