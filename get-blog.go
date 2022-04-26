package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	DEVAPIKEY := os.Getenv("DEVAPIKEY")
	client := &http.Client{}
	req, err := http.NewRequest("GET", "https://dev.to/api/articles/me/unpublished", nil)
	if err != nil {
		log.Fatal(err)
	}
	req.Header.Set("api-key", DEVAPIKEY)
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	defer resp.Body.Close()
	bodyText, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", bodyText)
}
