# Downloading body pose (MPI) model...
MPI_FOLDER="$1"
# 
wget -c "https://www.uio.no/ritmo/english/research/labs/fourms/software/musicalgesturestoolbox/mgt-python/pose-models/mpi/pose_iter_160000.caffemodel" -P ${MPI_FOLDER} --no-check-certificate 
# Download finished.