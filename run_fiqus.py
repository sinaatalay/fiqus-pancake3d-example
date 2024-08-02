import platform
import pathlib

from fiqus import MainFiQuS

root_path = pathlib.Path(__file__).parent

# check if it is Windows, Linux or Mac and set the path to GetDP accordingly
binaries_path = root_path / "bin"
if platform.system() == "Windows":
    getdp_path = binaries_path / "cerngetdp_mpi_2024.7.2.exe"
elif platform.system() == "Linux":
    getdp_path = binaries_path / "cerngetdp_2024.7.2"
elif platform.system() == "Darwin":
    raise NotImplementedError("CERNGetdp is not available for Mac OS yet!")


# run FiQuS with pancake3Dexample_fiqus.yaml:
output_folder = root_path / "output"
MainFiQuS.MainFiQuS(
    GetDP_path=getdp_path,
    input_file_path="HTSPancakeCoil_FiQuS.yaml",
    model_folder=output_folder,
)
