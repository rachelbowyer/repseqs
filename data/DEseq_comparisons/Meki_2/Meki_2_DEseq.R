##This script calculates differential expression between two different samples
library(DESeq)
library(dplyr)


#edit file name
file_name=c('Meki_2')


setwd(paste0('~/software_engineering_for_scientists/quiescence_project/repseqs/data/DEseq_comparisons/', file_name, '/'))
dataFile_raw = read.delim(paste0(file_name,'.csv'),sep=',',header=TRUE,row.names=2)
dataFile <- select(dataFile_raw, 4:7)

##edit experiment design
dataDesign = data.frame(rows.name=colnames(dataFile),condition=c("Exp","Exp","Ctl","Ctl"), 
                        libType=c("single-end","single-end","single-end","single-end","single-end"))
condition = factor(c("Exp","Exp","Ctl","Ctl"))


#The rest should run without modification
cds = newCountDataSet(dataFile,condition)
cds = estimateSizeFactors(cds)
sizeFactors(cds)
normTable = counts(cds,normalized=TRUE)
write.table(normTable,paste0(file_name, '.txt'),quote=FALSE,sep='\t')
cds = estimateDispersions(cds, method='pooled')
str(fitInfo(cds))
png(paste0(file_name, '.png'))
plotDispEsts(cds)
dev.off()
res = nbinomTest(cds,"Exp","Ctl")
png(paste0(file_name, '.png'))
plotMA(res, ylim=c(-8,8))
##take out infinite values and NaN values and replot MA plot
#convert res to tbl and remove -Inf and Inf values
tbl_res <- tbl_df(res)
tbl_res_no_inf <- filter(tbl_res, log2FoldChange != -Inf, log2FoldChange != Inf)
png(paste0(file_name, '.png'))
plotMA(tbl_res_no_inf)

dev.off()
resSig = res[ res$padj < 0.05, ]
resSig = res
resSig = resSig[ order(resSig$pval), ]

#add info to no_inf_file


write.table(resSig,paste0(file_name, '_output.csv'),quote=FALSE,sep=',',row.names=FALSE)
write.table(tbl_res_no_inf,paste0(file_name, '_output_no_inf.csv'),quote=FALSE,sep=',',row.names=FALSE)
savehistory(file=paste0(file_name, '.txt'))

