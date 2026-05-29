package main
import "fmt"

func add( a int, b int )int{
	return a + b
}

func main(){
	nums := []int{1,2,3,4,5}
	m := map[string]int{
		"even" : 0,
		"odd" : 0,
	}
	for i := 0; i < len(nums); i++{
		if nums[i]%2 == 0{
			m["even"] += nums[i]
		}else{
			m["odd"] += nums[i]
		}

	}
	fmt.Println(m["even"])
	fmt.Println(m["odd"])
}