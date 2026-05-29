package main
import "fmt"
import "github.com/gin-gonic/gin"

func main(){
	r := gin.Default()
	r.GET("/",body)
	r.RUN(":8000")
}
func body(c *gin.Context){
	c.JSON()
}