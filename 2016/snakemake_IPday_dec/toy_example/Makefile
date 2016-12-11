SAMPLES = sample_A sample_B
FASTQS = $(patsubst %,%.fastq.gz,$(SAMPLES))

ODIR = "mapped_sample"
BAMS = $(patsubst %,$(ODIR)/%.bam,$(SAMPLES))

INDEX =  phiX174.fa.bwt
REFERENCE =  phiX174.fa

# Main rule
all: $(BAMS)

# $< means first element in the list
# $@ means left hand side of the rule :
# bwa_mapping
$(ODIR)/%.bam: %.fastq.gz $(INDEX) $(ODIR)
	bwa mem $(REFERENCE) $< | samtools view -Sb - > $@

$(ODIR):
	mkdir -p $(ODIR)

# bwa_index
$(INDEX): $(REFERENCE)
	bwa index $<

clean:
	rm -f phiX174.fa.* *.bam 
	rm -rf $(ODIR)
