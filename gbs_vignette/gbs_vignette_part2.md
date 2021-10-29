# GBS vignette part 2

## cleaning up your directories and converting sams to bams

The files you are working with are very large, so it is very important to zip your files once you are finished working with them. Once your `run_bwa.py` wrapper is finished (you can check if the process is still running with `htop`), we won't be working with the `fastq` files anymore, so go ahead and zip all of them. This will take a bit, so use the `&` to run the process in the background.

      $ gzip *.fastq &

Now take a look in the new `sam_sai` directory. You'll see that the `run_bwa.py` wrapper produced a `sam` and a `sai` file for each individual. The `sam` files contain all of the information about the read mapping to your reference based assembly. Use `less` to take a look inside of a sam file to familiarize yourself with the file format. The next steps of the pipeline require the `sam` files to be converted to binary `bam` files. We will be using another Python wrapper (`sam2bam.py`) for this conversion. Move the wrapper into the `sam_sai` directory and execute it on your `sam` files. You will need to load the program `samtools` before execution.

      $ module load samtools/1.3
      $ python3 sam2bam.py *.sam

The `sam` files are very large, so once the `sam2bam.py` wrapper has finished running, kill the `sam` and `sai` files using `rm`.

      $ rm *.sam
      $ rm *.sai


## Calling variants

We will be using the programs `samtools` and `bcftools` to call variants (i.e., find SNPs) in our dataset. This process will ultimately construct a `vcf` file that will contain information about the genotypes of individual sheep at every variable position in the genome that we sampled in our dataset. You will want to place the job in the background after you know it is working appropriately (control-Z, `bg`, `disown -h`). 

      $ module load samtools/1.3
      $ module load bcftools/1.3
      $ samtools mpileup -P ILLUMINA --BCF --max-depth 100 --adjust-MQ 50 --min-BQ 20 --min-MQ 20 --skip-indels --output-tags AD,DP --fasta-ref ../bighorn_genome.fa aln*sorted.bam | bcftools call -m --variants-only --format-fields GQ --skip-variants indels | bcftools filter --set-GTs . -i 'QUAL > 19 && FMT/GQ >9' | bcftools view -m 2 -M 2 -v snps --apply-filter "PASS" --output-type v --output-file variants_rawfiltered.vcf


After you have finished calling variants, remember to clean up your directories. You will need to zip `bighorn_ref.fa` using the `gzip` command.


## Filtering variants

You now have a file `sam_sai` directory named `variants_rawfiltered.vcf`. This file contains all of the information about variable sites (i.e. SNPs) in your dataset. Use `less` and `tail` to investigate the format of the `vcf` file. Then use `grep` to count how many variable sites are found in your raw file.

      $ grep -c "^CP" variants_rawfiltered.vcf

For a lot of different reasons, we do not want to use all of the variant sites in the raw vcf file. Instead, we will filter out some loci that don’t meet certain thresholds that we will set. First we need to format our `vcf` file using `bcftools`. To do so, we will use some Unix commands to make an ids file (`sheep_ids_col.txt)`. After this step, zip all of your `bam` and `bai` files using `gzip`.

      $ module load bcftools/1.3
      $ ls *sorted.bam > bams.txt
      $ sed "s/aln_//" bams.txt | sed -s "s/.sorted.bam//" > sheep_ids_col.txt
      $ bcftools reheader -s sheep_ids_col.txt variants_rawfiltered.vcf -o rehead_variants_rawfiltered.vcf
      $ gzip *.bam &
      $ gzip *.bai &


For our first filtering step, we will remove all variant sites that have minor allele frequencies (maf) less than 0.05. These loci could result from sequencing errors, and are often removed from next-generation sequencing datasets.

      $ module load vcftools/0.1.14
      $ vcftools --vcf rehead_variants_rawfiltered.vcf --out variants_maf0.05 --remove-filtered-all --maf 0.05 --recode --thin 90

This should remove roughly half of your loci, which is ok. We still have a lot of loci to work with. Next we will remove all loci that did not have a read sequenced in at least 80% of the individuals.

      $ vcftools --vcf variants_maf0.05.recode.vcf --out variants_maf0.05_miss20 --remove-filtered-all --max-missing 0.8 --recode


After these filtering steps, you should now have a dataset of 20 individuals and roughly 18,168 SNPs. There are several other filtering steps that you would complete if you were actually working on this dataset, but hopefully this gives you some idea of what that process looks like. Now we will export the data into a file format that we can use to run analyses using the `--012` flag. This command will produce a dataset containing 0's, 1's, 2's, and -1's, where zero corresponds to the first homozygous state (e.g., AA), two corresponds to the second homozygous state (e.g., TT), one corresponds to the heterozygous state (e.g., AT), and -1 corresponds to missing/uncertain data. Importantly, the analyses that we need run do not accept -1's as missing data, so we need to change the -1's into NA's using `sed`.

      $ vcftools --vcf variants_maf0.05_miss20.recode.vcf --012
      $ sed 's/-1/NA/g' out.012 > out.012_NAs


You will also need to create a population ids file. We will create this from an individual ids file that was also created by the last vcftools command (`out.012.indv`). The ids contain subspecies, herd, and individual identifier information separated by underscores, and we want to `cut` only the first two pieces of information for our population ids file.

      $ cut -f 1,2 -d "_" out.012.indv > sheep_pops.txt

You have now finished everything you need to do on ponderosa. Please zip all of the `vcf` files before exiting the server

      $ gzip *.vcf &



## population genetic analyses

You will be running a principal component analysis (PCA) with `R` on your laptop to investigate patterns of genetic structure in the dataset you just created. If you do not have `R` or `RStudio` installed on your computer, please do so now.

You will also need to transfer `out.012.NA` and `sheep_pops.txt` to your laptop using `scp`. Move to the directory on your laptop where you want to store these files and execute the commands below. NOTE: the example `scp` commands below are for group1, so other groups will need to change their group number before executing the commands.

      $ scp group1@ponderosa.biology.unr.edu:/working/group1/sam_sai/out.012_NAs .
      $ scp group1@ponderosa.biology.unr.edu:/working/group1/sam_sai/sheep_pops.txt .


Once you open `R`, you will need to change your working directory using the `setwd` command (you can use the Unix command `pwd` in the terminal to find the full path to your directory).

      > setwd("FULL_PATH_TO_WHERE_YOUR_FILES_ARE")
      > sheep <- read.delim("out.012_NAs", header=F)
      > good_sheep <- sheep[,-1]
      > pops <- read.delim("sheep_pops.txt", header=F)
      > sheep_mn <- apply(good_sheep, 1, mean, na.rm=TRUE)
      > sheep_mnmat <- matrix(sheep_mn, nrow=18168, ncol=20)
      > sheep_prime <- t(good_sheep) - sheep_mnmat
      > sheep_covarmat <- matrix(NA, 20, 20)
      
      > for (i in 1:20) {
            for (j in 1:20) {
                  if (i==j) {
                        sheep_covarmat[i,j] <- cov(sheep_prime[,i], sheep_prime[,j], use="pairwise.complete.obs")
                        }
                  else {
                        sheep_covarmat[i,j] <- cov(sheep_prime[,i], sheep_prime[,j], use="pairwise.complete.obs")
                        sheep_covarmat[j,i] <- sheep_covarmat[i,j]
                        }
                  }
            }
      
      > pca <- prcomp(sheep_covarmat, center=TRUE, scale=FALSE)
      > summary(pca)


You now have created an object (pca) that contains all of the results from the analysis. Use the following commands to create a plot

      > quartz(height=6, width=6)
      > par(mar=c(5,5,1,1))
      > plot(pca$x[,1], pca$x[,2], xlab="PC 1 (32.5% variance explained)", ylab="PC 2 (14.5% variance explained)", type="n")
      > points(pca$x[pops=="DB_212", 1], pca$x[pops=="DB_212", 2], pch=21, bg="#7c67f2", cex=2, lwd=2)
      > points(pca$x[pops=="DB_271", 1], pca$x[pops=="DB_271", 2], pch=21, bg="#edc213", cex=2, lwd=2)
      > points(pca$x[pops=="DB_269", 1], pca$x[pops=="DB_269", 2], pch=21, bg="#007ea8", cex=2, lwd=2)
      > points(pca$x[pops=="DB_268", 1], pca$x[pops=="DB_268", 2], pch=21, bg="#a05000", cex=2, lwd=2)
      > legend("bottomleft", legend=c("Mormon Mtns. (271)", "Muddy Mtns. (268)", "Lone Mtn. (212)", "River Mtns. (269)"), pch=21, pt.bg=c("#edc213", "#a05000", "#7c67f2", "#007ea8"), cex=1.25, pt.cex=2, pt.lwd=2)


Congrats! You’ve made it through the entire module, and have recreated Figure 2A from our bighorn sheep paper (you can find the paper on github if you are interested). You can see that there is strong genetic differentiation among these four bighorn sheep herds.


## Required tasks to be completed

1) Email Tom and Josh a pdf of the PCA plot that you just made. 2) Celebrate your success. 3) Say thank you to the next bighorn sheep you see.




