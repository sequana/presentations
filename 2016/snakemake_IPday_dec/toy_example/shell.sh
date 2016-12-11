#!/bin/sh
REFERENCE="phiX174.fa"

OUTDIR="mapped_sample"
SAMPLES=`ls *.fastq.gz` 


function bwa_index
{
    bwa index $REFERENCE
}

function makedir
{
    mkdir -p $OUTDIR
}

function bwa_mem
{
for var in $SAMPLES
do
    TARGET=${var/.fastq.gz/.bam}
    bwa mem $REFERENCE $SAMPLES | samtools view -Sb - > $OUTDIR/$TARGET
done
}

echo $1

if [ "$1" == "all" ]; then
    $(bwa_index)
    $(makedir)
    $(bwa_mem)
fi

if [ "$1" == "bwa_index" ]; then
    $(makedir)
    $(bwa_index)
fi

if [ "$1" == "bwa_mem" ]; then
    $(makedir)
    $(bwa_index)
    $(bwa_mem)
fi

if [ "$1" == "makedir" ]; then
    $(makedir)
fi
