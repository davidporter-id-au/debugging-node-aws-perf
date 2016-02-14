package main

import (
	"fmt"
	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/dynamodb"
	"time"
)

func getRecord(svc *dynamodb.DynamoDB, tableName string, key string) {
	params := &dynamodb.GetItemInput{
		Key: map[string]*dynamodb.AttributeValue{
			"key": {
				S: aws.String(key),
			},
		},
		TableName: aws.String(tableName),
	}
	_, err := svc.GetItem(params)
	if err != nil {
		fmt.Println(err.Error())
		return
	}
}

func main() {
	svc := dynamodb.New(session.New(), &aws.Config{Region: aws.String("ap-southeast-2")})
	for {
		start := time.Now()
		getRecord(svc, "test", "FOO")
		elapsed := time.Since(start)
		fmt.Println(elapsed)
		time.Sleep(time.Second * 1)
	}
}
