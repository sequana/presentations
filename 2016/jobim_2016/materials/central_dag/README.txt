The pipeline quality_variant is not for production. It is the merging of
quality_taxon (include) and a copy/paste of variant_calling. We add to manually
change the  input of the rule bwa_mem_ref with the output of quality_taxon
(__cutadapt__output). The final pipeline is not functional since the config file
is not;. Besides you will need to provide some input files.

Then, type::

    snakemake -s quality_variant --dag

There is an error but the dag is produced. We then manually edited dag.dot
to create sub-graph in the graphviw dot file
