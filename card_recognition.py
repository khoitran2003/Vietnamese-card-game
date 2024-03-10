import torch
import cv2
import numpy as np


class CardRecognition:

    def __init__(self, cards, kind="Tien Len"):
        self.cards = cards
        self.kind = kind
        self.ranking_card = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]
        self.ranking_digit_card = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.ranking_alphabet_card = ["J", "Q", "K", "A"]

    def sort_card_without_second_name(self, cards):
        cards = [str(c[:-1]) for c in cards]
        num_list = [str(x) for x in sorted([int(x) for x in cards if x.isdigit()])]
        alpha_list = [x for x in cards if x.isalpha()]
        alpha_list.sort(key=lambda x: self.ranking_alphabet_card.index(x))
        sorted_card = num_list + alpha_list
        return sorted_card

    def sort_card_with_second_name(self, cards):
        cards_values = [c[:-1] for c in self.cards]
        sorted_values = sorted(cards_values, key=lambda x: self.ranking_card.index(x))
        sorted_values = [
            value + x for value, x in zip(sorted_values, [c[-1] for c in cards])
        ]
        return sorted_values

    def ls2str(self, ls):
        string = ""
        for x in ls:
            string += str(x) + " "
        return string

    def detect(self):
        result = None
        if self.kind == "Tien Len":
            sc = self.sort_card_without_second_name(self.cards)
            if len(sc) == 1:
                result = "Coc: {}".format(self.ls2str(self.cards))
            if len(sc) == 2:
                unique_card = set(sc)
                if len(unique_card) == 1:
                    result = "Doi: {}".format(self.ls2str(self.cards))
                else:
                    result = "Khong phai doi"
            if len(sc) > 2:
                unique_card = set(sc)
                if len(sc) == 3:
                    if len(unique_card) == 1:
                        result = "Tam: {}".format(self.ls2str(self.cards))
                    elif len(unique_card) == 3:
                        result = "Sanh 3: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                if len(sc) == 4:
                    if len(unique_card) == 1:
                        result = "Tu quy: {}".format(self.ls2str(self.cards))
                    elif len(unique_card) == 4:
                        result = "Sanh 4: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                if len(sc) in [5, 7, 9, 11, 13]:
                    result = "Sanh {}: {}".format(
                        len(sc),
                        self.ls2str(self.sort_card_with_second_name(self.cards)),
                    )
                if len(sc) == 6:
                    if len(unique_card) == 3:
                        result = "Ba doi thong: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                    elif len(unique_card) == 6:
                        result = "Sanh 6: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                if len(sc) == 8:
                    if len(unique_card) == 4:
                        result = "Bon doi thong: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                    elif len(unique_card) == 8:
                        result = "Sanh 8: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                if len(sc) == 10:
                    if len(unique_card) == 5:
                        result = "Nam doi thong: {}".format(self.ls2str(self.cards))
                    elif len(unique_card) == 8:
                        result = "Sanh 10: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
                if len(sc) == 12:
                    if len(unique_card) == 6:
                        result = "Sau doi thong: {}".format(self.ls2str(self.cards))
                    elif len(unique_card) == 8:
                        result = "Sanh 12: {}".format(
                            self.ls2str(self.sort_card_with_second_name(self.cards))
                        )
            return result

        if self.kind == "Ba Cao":
            sc = self.sort_card_without_second_name(self.cards)
            if len(sc) == 3:
                if sum([True if x in ["J", "K", "Q"] else False for x in sc]) == 3:
                    result = "Ba Tay"
                else:
                    result = [10 if x in ["J", "K", "Q"] else x for x in sc]
                    result = [1 if x == "A" else x for x in result]
                    result = sum(list(map(int, result))) % 10
                    if result == 0:
                        result = "Bu"
                    else:
                        result = "{} Nut".format(result)
            return result

        if self.kind == "Xi Dach":
            sc = self.sort_card_without_second_name(self.cards)
            unique_card = set(sc)
            if len(sc) == 1:
                result = "Khong phai Xi Dach"
            if len(sc) == 2:
                if len(list(unique_card)) == 1:
                    if list(unique_card)[0] in ["A"]:
                        result = "Xi Bang"
                    if list(unique_card)[0] in ["J", "K", "Q"]:
                        result = "20 diem"
                elif sum([True if x == "A" else False for x in sc]) == 1:
                    result = "Xi Dach"
                else:
                    result = [10 if x in ["J", "K", "Q"] else x for x in sc]
                    result = [11 if x == "A" else x for x in result]
                    result = "{} diem".format(sum(list(map(int, result))))
            if len(sc) == 3:
                result = [10 if x in ["J", "K", "Q"] else x for x in sc]
                result_0 = [10 if x == "A" else x for x in result]
                result_1 = sum(list(map(int, result_0)))
                if result_1 > 21:
                    result_0 = [1 if x == "A" else x for x in result]
                    result_1 = sum(list(map(int, result_0)))
                    if result_1 <= 21:
                        result = "{} diem".format(result_1)
                    else:
                        result = "{} diem. Quac!".format(result_1)
                else:
                    result = "{} diem".format(result_1)
            if len(sc) == 4:
                result = [10 if x in ["J", "K", "Q"] else x for x in sc]
                result = [1 if x == "A" else x for x in result]
                result = sum(list(map(int, result)))
                if result > 21:
                    result = "{} diem. Quac!".format(result)
                else:
                    result = "{} diem".format(result)
            if len(sc) == 5:
                result = [10 if x in ["J", "K", "Q"] else x for x in sc]
                result = [1 if x == "A" else x for x in result]
                result = sum(list(map(int, result)))
                if result > 21:
                    result = "{} diem. Quac!".format(result)
                else:
                    result = "{} diem. Ngu Linh!".format(result)
            return result
