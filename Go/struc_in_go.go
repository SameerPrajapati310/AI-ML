// package main
// import (
// 	"fmt"
// 	"encoding/json"
// )

// type Message struct{
// 	Role string `json:"role"`
// 	Content string `json:"content"`
// }

// func main(){
// 	var message []Message
// 	message = append(message,Message{
// 		Role : "User",
// 		Content : "Hi my name is sameer",
// 	})
// 	message = append(message,Message{
// 		Role : "AI",
// 		Content : "Hi Nice to meet u",
// 	})
// 	JsonBody,err := json.Marshal(message)
// 	fmt.Println(string(JsonBody))
// 	if err != nil{
// 		fmt.Println("Hi an error occured")
// 	}
// 	for _,msg := range message{
// 		fmt.Printf("%s : %s\n",msg.Role,msg.Content)
// 	}
// }


// package main 
// import (
// 	"fmt"
// 	"net/http"
// 	"io"
// 	"encoding/json"
// )
// type Post struct{
// 	Body string `json:"body"`
// }

// func main(){
// 	client := &http.Client{}
// 	// create 
// 	req,err := http.NewRequest("GET","https://jsonplaceholder.typicode.com/posts/1",nil)
// 	if err != nil {
// 		fmt.Println("An error occured while creating request")
// 	}
// 	response,err := client.Do(req)
// 	if err != nil {
// 		fmt.Println("An error occured while sending request")
// 	}
// 	defer response.Body.Close()

// 	body,err := io.ReadAll(response.Body)
// 	if err != nil {
// 		fmt.Println("I am not able to print the final answer")
// 	}
// 	post := Post{}
// 	fmt.Println(string(body))
// 	json.Unmarshal(body,&post)
// 	fmt.Println(post.Body)

// }

