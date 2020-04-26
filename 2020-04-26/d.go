package main
import "fmt"
import "strconv"
func main(){
	var n string
	fmt.Scan(&n)
	var count int = 0
	var n_len int = len(n)
	for cut_length:=3; cut_length <= n_len ;cut_length++{
		for first:=0 ; first < n_len - cut_length ;first++{
			var tem string = n[first:first + cut_length+1]
			var cuted_num int
			cuted_num, _ = strconv.Atoi(tem)
//			fmt.Println(tem)
			if cuted_num % 2019 == 0 {
				count++
			}
		}
	}  
	fmt.Println(count)
}