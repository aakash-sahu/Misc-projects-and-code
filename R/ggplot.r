# R code snippet used for making charts and pdf using ggplot2 with common legend

#---->Creating charts....

BS_Charts <- list()
unq_mnemonics <- unique(df$MNEMONIC)
counter <- length(unq_mnemonics)
                      
#---->Creating common legend....
g_legend<-function(a.gplot){
  tmp <- ggplot_gtable(ggplot_build(a.gplot))
  leg <- which(sapply(tmp$grobs, function(x) x$name) == "guide-box")
  legend <- tmp$grobs[[leg]]
  return(legend)}


#---->Storing charts....
for(i in 1:counter){
  BS_Charts [[i]] <- list()
  BS <- filter(df, MNEMONIC == unq_mnemonics[i])
  BS_Charts[[i]][[1]] <- ggplot(data= BS,mapping = aes(x= QUARTER, y= VALUE, color = SCENARIO, group = SCENARIO)) +
    geom_point() +
    geom_line(linetype = 2) +
    labs(x = NULL,y= paste('Value in',BS$UNIT_CODE), 
       title =  paste('\n',BS$COUNTRY, BS$DESCRIPTION),
      subtitle =paste('\nMnemonic =',BS$MNEMONIC)
       ) +
        theme(plot.margin = unit(c(1,0.8,0.25,0.6), "lines"),
          legend.position ="bottom",
          axis.title.y = element_text(size = rel(0.7)),
          axis.text = element_text(size = rel(0.7)),
          axis.text.x = element_text(angle = 15, hjust = 0.5),
          plot.title = element_text(size = rel(0.9), face = "bold",hjust = 0.5),
          plot.subtitle = element_text(size = rel(0.9),hjust = 1),
          legend.title = element_text(size = rel(0.6), face = "italic"),
          legend.text = element_text(size = rel(0.7), face = "italic"),
          legend.background = element_rect(color = "grey")
          )
  
  BS_Charts[[i]][[2]] <- ggplot(data= BS,mapping = aes(x= QUARTER, y= QONQ_GROWTH, color = SCENARIO, group = SCENARIO)) +
    geom_point() +
    geom_line(linetype = 3) +
    labs(x = NULL,y= paste('%'), subtitle =  '\n\nQuarter on Quarter Growth Rate') +
    theme(plot.margin = unit(c(1,0.8,0.5,0.6), "lines"),
          legend.position ="bottom",
          axis.title.y = element_text(size = rel(0.7)),
          axis.text = element_text(size = rel(0.7)),
          plot.subtitle = element_text(size = rel(0.9),hjust = 1),
          axis.text.x = element_text(angle = 15, hjust = 0.5),
          plot.title = element_text(size = rel(0.9), face = "bold",hjust = 0.5),
          legend.title = element_text(size = rel(0.6), face = "italic"),
          legend.text = element_text(size = rel(0.7), face = "italic"),
          legend.background = element_rect(color = "grey")
    )
}                      

#---->Printing two charts....
BS_Charts[[2]][[1]] 
BS_Charts[[2]][[2]]
                      

#---->Creating pdf with all plots....
pdf("Balance Sheet Factors.pdf", onefile = TRUE)

plot(0:10, type = "n", xaxt="n", yaxt="n", bty="n", xlab = "", ylab = "")
text(5, 10, "Forecasted data \n used in Balance Sheet Forecast")
text(5, 8,  "DFAST 2017")

 for (i in seq(1, length(BS_Charts))) {
  grid.arrange(arrangeGrob(BS_Charts[[i]][[1]] + theme(legend.position="none"),
                           BS_Charts[[i]][[2]] + theme(legend.position="none"),
                                                      nrow=2),
               g_legend(BS_Charts[[i]][[1]]), nrow=2,heights=c(5,1))  
}
dev.off() 
                      
