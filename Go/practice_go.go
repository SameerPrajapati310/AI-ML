package main
import (
	"fmt"
	"encoding/json"
	"net/http"
)

type User struct{
	Id : int `json:"id"`
	Name : string `json:"name"`
	Email : string 	`json:"email"`
}

var users []User

func create_user(w http.ResponseWriter, r *http.Request){
	if r.Method != w.MethodPost {
		http.Error(w,"Error getting request")
		return 
	}
	var user User
	json.NewDecode(r.Body).Decode(&user)
	user.Id = 1
	users = append(users,user)
	w.SetHeaders("Conten-Type","appkication-json")
	json.NewEncode(w).Encode(user)
}

func main(){
	http.HandleFunc("/users",create_user)
	http.ListenAndServe(":8080")
}