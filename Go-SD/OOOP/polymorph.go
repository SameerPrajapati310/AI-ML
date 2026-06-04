package main

import "fmt"

type Car interface {
	StartEngine()
	StopEngine()
	AccelerateEngine()
	ChangeGear()
}

type BaseCar struct {
	Model string
	Brand string
	Speed int
}

func (b *BaseCar) StartEngine() {
	fmt.Println("Engine Started")
}

func (b *BaseCar) StopEngine() {
	fmt.Println("Engine Stopped")
}

type Manual struct {
	BaseCar
	Gear int
}

func NewManual(m string, b string) *Manual {
	return &Manual{
		BaseCar: BaseCar{
			Model: m,
			Brand: b,
			Speed: 0,
		},
		Gear: 0,
	}
}

func (m *Manual) AccelerateEngine() {
	fmt.Println("Speed of the engine has been increased")
}

func (m *Manual) ChangeGear() {
	m.Gear++
	fmt.Println("Gear changed to", m.Gear)
}

func main() {
	car := NewManual("TCS", "TATA")

	car.StartEngine()
	car.AccelerateEngine()
	car.ChangeGear()
	car.StopEngine()
}
