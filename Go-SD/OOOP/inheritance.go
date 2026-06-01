package main

import "fmt"

type Car struct {
	Brand   string
	Model   string
	isStart bool
	speed   int
}

func NewCar(b string, m string) *Car {
	return &Car{
		Brand:   b,
		Model:   m,
		isStart: false,
		speed:   0,
	}
}

func (c *Car) startCar() {
	c.isStart = true
	fmt.Println("Car started")
}

func (c *Car) incSpeed() {
	if c.isStart == false {
		fmt.Println("Engine is not started!!!")
		return
	}

	c.speed += 20
	fmt.Println("Speed of the car has been increased")
	fmt.Println("Current Speed:", c.speed)
}

/////////////////////////////////////////////////

type Battery struct {
	Car
	BatteryLevel int
}

func NewBattery(b string, m string) *Battery {
	return &Battery{
		Car:          *NewCar(b, m),
		BatteryLevel: 100,
	}
}

/////////////////////////////////////////////////

func main() {

	car := NewCar("Tata", "XUV")
	car.startCar()
	car.incSpeed()

	fmt.Println("----------------")

	bcar := NewBattery("Tesla", "Model S")
	bcar.startCar()
	bcar.incSpeed()
}