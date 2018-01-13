#pragma once
#include "node.hpp"
#include <cmath>
#include <iomanip>
#include <iostream>
#include <tuple>
#include <vector>

#define MIN_VALUE_OF_M 3

template <typename Key, typename Value, std::uint16_t M>
class BTree {
public:
    BTree()
        : root(nullptr)
    {
        static_assert(MIN_VALUE_OF_M <= M, "M parameter have to be equal or greater than MIN_VALUE_OF_M");
    };
    void insert(const Key& key, const Value& value);
    std::pair<bool, Value> findFirst(const Key& key) const;
    std::vector<Value> find(const Key& key) const;
    bool erase(const Key& key);

private:
    Node<Key, Value, M>* root;
    void setRoot(const Key& key, const Value& value);
    void splitNodes(Node<Key, Value, M>* temp, Node<Key, Value, M>* parent);
    void print(Node<Key, Value, M>* node, int indent);
    std::tuple<Node<Key, Value, M>*, Node<Key, Value, M>*> findWhereToAddNode(const Key& key);
};

template <typename Key, typename Value, std::uint16_t M>
void BTree<Key, Value, M>::print(Node<Key, Value, M>* node, int indent)
{
    Node<Key, Value, M>* tmp = node;
    for (auto n : node->childs) {
        if (n.first != nullptr) {
            std::cout << "left" << std::endl;
            print(n.first, indent + 4);
        }

        if (indent) {
            std::cout << std::setw(indent) << ' ';
        }
        std::cout << "node " << n.second.first << std::endl;

        if (tmp->right != nullptr) {
            std::cout << "right" << std::endl;
            print(tmp->right, indent + 4);
            tmp = tmp->right;
        }
    }
}

template <typename Key, typename Value, std::uint16_t M>
void BTree<Key, Value, M>::setRoot(const Key& key, const Value& value)
{
    root = new Node<Key, Value, M>();
    root->add(nullptr, std::make_pair(key, value));
}

template <typename Key, typename Value, std::uint16_t M>
std::vector<Value> BTree<Key, Value, M>::find(const Key& key) const
{
    std::vector<Value> vec;
    Node<Key, Value, M>* tmp = root;
    while (tmp) {
        for (auto& pairs : tmp->childs) {
            if (key == pairs.second.first) {
                vec.push_back(pairs.second.second);
            } else if (key < pairs.second.first) {
                tmp = pairs.first;
                break;
            } else if (key < pairs.second.first && key > pairs.second.first) {
                tmp = pairs.first;
                break;
            }
            if (pairs == tmp->childs.back()) {
                tmp = tmp->right;
            }
        }
    }
    return vec;
}

template <typename Key, typename Value, std::uint16_t M>
std::pair<bool, Value> BTree<Key, Value, M>::findFirst(const Key& key) const
{
    Node<Key, Value, M>* tmp = root;
    while (tmp) {
        for (auto& pairs : tmp->childs) {
            if (key == pairs.second.first) {
                return std::make_pair(true, pairs.second.second);
            } else if (key < pairs.second.first) {
                tmp = pairs.first;
                break;
            } else if (key < pairs.second.first && key > pairs.second.first) {
                tmp = pairs.first;
                break;
            } else if (pairs == tmp->childs.back()) {
                tmp = tmp->right;
            }
        }
    }

    return std::make_pair(false, Value());
}

template <typename Key, typename Value, std::uint16_t M>
std::tuple<Node<Key, Value, M>*, Node<Key, Value, M>*> BTree<Key, Value, M>::findWhereToAddNode(const Key& key)
{
    Node<Key, Value, M>* temp = root;
    Node<Key, Value, M>* parent = root;

    while (temp->right) {
        if (temp->getAmountOfChild() > M - 1) {
            splitNodes(temp, parent);
        }
        if (temp->getAmountOfChild() == 1) {
            if (key <= temp->getNdKey(0)) {
                parent = temp;
                temp = temp->childs[0].first;
            } else {
                parent = temp;
                temp = temp->right;
            }
            continue;
        }
        for (int i = 1; i < temp->getAmountOfChild(); ++i) {
            if (key <= temp->getNdKey(i - 1)) {
                parent = temp;
                temp = temp->childs[i - 1].first;
                break;
            } else if (key >= temp->getNdKey(i) && key <= temp->getNdKey(i - 1)) {
                parent = temp;
                temp = temp->childs[i].first;
                break;
            } else if (i == temp->getAmountOfChild() - 1) {
                parent = temp;
                temp = temp->right;
            }
        }
    }
    return std::make_tuple(temp, parent);
}

template <typename Key, typename Value, std::uint16_t M>
void BTree<Key, Value, M>::insert(const Key& key, const Value& value)
{
    if (root == nullptr) {
        setRoot(key, value);
        return;
    }

    Node<Key, Value, M>*temp, *parent;
    std::tie(temp, parent) = findWhereToAddNode(key);

    temp->add(nullptr, std::make_pair(key, value));

    if (temp->getAmountOfChild() > M - 1) {
        splitNodes(temp, parent);
    }

    std::cout << "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&" << std::endl;
    print(root, 0);
    std::cout << "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&" << std::endl;
}

template <typename Key, typename Value, std::uint16_t M>
void BTree<Key, Value, M>::splitNodes(Node<Key, Value, M>* temp, Node<Key, Value, M>* parent)
{
    Node<Key, Value, M>* node = new Node<Key, Value, M>(nullptr,
                                                        new Node<Key, Value, M>(temp->childs[std::ceil(M / 2)].first,
                                                                                temp->childs[0].first,
                                                                                temp->childs[0].second),
                                                        temp->childs[std::ceil(M / 2)].second);
    node->right = new Node<Key, Value, M>(temp->right,
                                         temp->childs[M - 1].first,
                                         temp->childs[M - 1].second);
    parent->right = node->right;

    if (parent == root && parent->getAmountOfChild() == M) {
        parent->childs = node->childs;
    } else {
        parent->add(node->childs[0].first, node->childs[0].second);
    }
}
