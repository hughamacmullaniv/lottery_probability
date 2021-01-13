> k_table <- cbind(c(0,1,2,3,4), c(0,0.5,1,1.5,0.5))
> Previous_Finishes = 5
> if ( Previous_Finishes <= max(k_table[,1]) ) {
+     k <- k_table[k_table[,1] == Previous_Finishes,][2]
+ } else {
+     k <- k_table[k_table[,1] == max(k_table[,1]),][2]
+ }
> k
[1] 0.5
> Previous_Finishes = 2
> if ( Previous_Finishes <= max(k_table[,1]) ) {
+     k <- k_table[k_table[,1] == Previous_Finishes,][2]
+ } else {
+     k <- k_table[k_table[,1] == max(k_table[,1]),][2]
+ }
> k
[1] 1
