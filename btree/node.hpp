#pragma once

#include <algorithm>
#include <iostream>
#include <vector>

template <typename Key, typename Value, std::uint16_t M>
struct Node {
    typedef std::pair<Node*, std::pair<Key, Value>> vectorType;
    Node* right;
    std::vector<vectorType> childs;

    Node(Node* right, Node* node, std::pair<Key, Value> pairVal)
        : right(right)
    {
        add(node, pairVal);
    }
    Node()
        : right(nullptr)
    {
    }

    void add(Node* node, std::pair<Key, Value> child);
    int getAmountOfChild();
    Key getStKey(int pos);
    Key getNdKey(int pos);
};

template <typename Key, typename Value, std::uint16_t M>
void Node<Key, Value, M>::add(Node* node, std::pair<Key, Value> child)
{
    auto it = std::lower_bound(childs.begin(), childs.end(), vectorType(node, child),
        [](const vectorType& l, const vectorType& r) { return l.second.first < r.second.first; }); // find proper position in descending order
    childs.insert(it, std::make_pair(node, child));
}

template <typename Key, typename Value, std::uint16_t M>
int Node<Key, Value, M>::getAmountOfChild()
{
    return childs.size();
}

template <typename Key, typename Value, std::uint16_t M>
Key Node<Key, Value, M>::getStKey(int pos)
{
  return childs[pos].first;
}

template <typename Key, typename Value, std::uint16_t M>
Key Node<Key, Value, M>::getNdKey(int pos)
{
  return childs[pos].second.first;
}
