#include "catch.hpp"
#include "btree.hpp"

TEST_CASE("Add nodes", "[btree]")
{
  BTree<int, std::string, 3> btree;
  btree.insert(1, "MOSKVA");                 //                       4 8
  btree.insert(2, "LONDON");                 //              2          6           11
  btree.insert(3, "BERLIN");                 //          1     3      5   7      9    11 12
  btree.insert(4, "MADRID");
  btree.insert(5, "ROMA");
  btree.insert(6, "KIEV");
  btree.insert(7, "PARIS");
  btree.insert(8, "BUCURESTI");
  btree.insert(9, "BUDAPEST");
  btree.insert(11, "Hamburg");
  btree.insert(11, "MINSK");
  btree.insert(12, "WARSZAWA");

  REQUIRE(btree.findFirst(1).second    == "MOSKVA");
  REQUIRE(btree.findFirst(2).second    == "LONDON");
  REQUIRE(btree.findFirst(3).second    == "BERLIN");
  REQUIRE(btree.findFirst(4).second    == "MADRID");
  REQUIRE(btree.findFirst(5).second    == "ROMA");
  REQUIRE(btree.findFirst(6).second    == "KIEV");
  REQUIRE(btree.findFirst(7).second    == "PARIS");
  REQUIRE(btree.findFirst(8).second    == "BUCURESTI");
  REQUIRE(btree.findFirst(9).second    == "BUDAPEST");
  REQUIRE(btree.findFirst(11).second    == "MINSK");
  REQUIRE(btree.findFirst(12).second    == "WARSZAWA");

  REQUIRE(btree.find(11).size()    == 2);
  REQUIRE(btree.find(11)[0]    == "MINSK");
  REQUIRE(btree.find(11)[1]    == "Hamburg");
}

