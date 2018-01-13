CXX      := g++
CXXFLAGS := -Wall -std=c++14 -pedantic -g -O2
DIR      := 'btree'
OBJS     := TestBTree.cpp
all:TestMain.o
	$(CXX) $(CXXFLAGS) TestMain.o $(OBJS) -o btree
TestMain.o: TestMain.cpp
	$(CXX) TestMain.cpp -c
run:
	./btree -r compact
tar: clean
	(cd ../; tar -cvzf $(DIR).tar.gz $(DIR))
.PHONY: clean
clean:
	rm -f *.o  *~ *.a *.so *.x core core* a.out *.exe btree *.gch

