package main
import "fmt"

type Car struct{
	Model string
	Brand string
	Speed int
	Start bool
}

func NewCar(m string, b string) *Car{
	return &Car{
		Model : m,
		Brand : b,
		Speed : 0,
		Start : false,
	}
}

func (c *Car) start(){
	fmt.Println("Hi lets get started")
	fmt.Printf("%s of %s started",c.Model,c.Brand)
}
func (c *Car) speed(){
	if c.Start == false{
		fmt.Println("Please start the car")
	}else{
		fmt.Printf("Speeeeeed of %s increased by +10 kmph\n",c.Model)
	}
}

func main(){
	car := NewCar("XUV","TaTa")
	car.start()
	car.speed()
}