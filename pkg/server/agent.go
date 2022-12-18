package server

import (
	"context"
	"fmt"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	pb "github.com/sekuradev/apigolang/sekuraapi/v1"
)

type serverAgent struct {
	pb.UnimplementedAgentServiceServer
}

func NewAgentServer() Server {
	return &serverAgent{}
}

func (s *serverAgent) Serve() {
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	gs := grpc.NewServer()
	pb.RegisterAgentServiceServer(gs, s)
	reflection.Register(gs)
	log.Printf("server listening at %v", lis.Addr())
	if err := gs.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}

func (s serverAgent) SetAccess(ctx context.Context, in *pb.SetAccessRequest) (*pb.SetAccessResponse, error) {
	fmt.Println("hello world")
	return &pb.SetAccessResponse{Error: false}, nil
}
