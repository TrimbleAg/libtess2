add_library(tess2 STATIC
    Source/bucketalloc.c
    Source/dict.c
    Source/geom.c
    Source/mesh.c
    Source/priorityq.c
    Source/sweep.c
    Source/tess.c
)
target_include_directories(tess2 PUBLIC Include)

install(FILES Include/tesselator.h DESTINATION include)
install(TARGETS tess2 DESTINATION lib)
