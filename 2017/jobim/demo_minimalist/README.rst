The gc_minimalist.rules snakefile simply reads FastQ files and create one GC
content histogram per file. Then, it creates a HTML page with all images
embedded in it.


sequanix -s gc_summary.rules -w .
