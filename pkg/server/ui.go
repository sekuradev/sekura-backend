package server

import (
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	pb "github.com/sekuradev/apigolang/sekuraapi/v1"
)

type serverUI struct {
	pb.UnimplementedUIServiceServer
}

func (s *serverUI) Serve() {
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	gs := grpc.NewServer()
	pb.RegisterUIServiceServer(gs, s)
	reflection.Register(gs)
	log.Printf("server listening at %v", lis.Addr())
	if err := gs.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

func NewUIServer() Server {
	return &serverUI{}
}
