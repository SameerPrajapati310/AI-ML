package main
import "fmt"

type BaseCar interface{
	StartCar()
	StopCar()
	Accelerate()
}

type Car struct {
	Model string
	Brand string
}

