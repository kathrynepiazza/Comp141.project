#!/usr/bin/Rscript

args <- commandArgs(trailingOnly = TRUE)

mean_val=as.numeric(args[1]) 
marginoferror=as.numeric(args[2])

upper_bound=mean_val+marginoferror
lower_bound=mean_val-marginoferror

write(sprintf("(%f, %f)", lower_bound, upper_bound), "")


