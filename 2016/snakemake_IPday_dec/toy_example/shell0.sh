#!/bin/sh
REFERENCE="phiX174.fa"
OUTDIR="mapped_sample"
SAMPLES=`ls *.fastq.gz` 


bwa index $REFERENCE

mkdir -p $OUTDIR

for var in $SAMPLES
do
    TARGET=${var/.fastq.gz/.bam}
    bwa mem $REFERENCE $SAMPLES | samtools view -Sb - > $OUTDIR/$TARGET
done
