#!/bin/usr/env python3

import random

import unicodedata

import typing

class ChineseCharacter(typing.NamedTuple):
    value: typing.Union[int,str]
    character: str
    pinyin: str 

def as_ascii(input: str):
    normalized = unicodedata.normalize('NFD', input)
    as_bytes = normalized.encode('ascii', 'ignore')
    return as_bytes.decode('ascii')

CHARACTERS = [
    ChineseCharacter('white', '白色', 'báisè'),
    ChineseCharacter('blue', '蓝色', 'lánsè'),
    ChineseCharacter('yellow', '黄色', 'huángsè'),
    ChineseCharacter('green', '绿色', 'lǜsè'),
    ChineseCharacter('red', '红色', 'hóngsè'),
    ChineseCharacter('orange1', '橘色', 'júsè'),
    ChineseCharacter('orange2', '橙色', 'chéngsè'),
    ChineseCharacter('brown', '咖啡色', 'kāfēisè'),
    ChineseCharacter('black', '黑色', 'hēisè'),
    ChineseCharacter('purple', '紫色', 'zǐsè'),
    ChineseCharacter('grey', '灰色', 'huīsè'),
    ChineseCharacter(0, '零', 'Líng'),
    ChineseCharacter(1, '一', 'Yī'),
    ChineseCharacter(2, '二', 'Èr'),
    ChineseCharacter(3, '三', 'Sān'),
    ChineseCharacter(4, '四', 'Sì'),
    ChineseCharacter(5, '五', 'Wǔ'),
    ChineseCharacter(6, '六', 'Liù'),
    ChineseCharacter(7, '七', 'Qī'),
    ChineseCharacter(8, '八', 'Bā'),
    ChineseCharacter(9, '九', 'Jiǔ'),
    ChineseCharacter(10, '十', 'Shí'),
    ChineseCharacter(11, '十一', 'Shíyī'),
    ChineseCharacter(12, '十二', 'Shíèr'),
    ChineseCharacter(13, '十三', 'Shísān'),
    ChineseCharacter(14, '十四', 'Shísì'),
    ChineseCharacter(15, '十五', 'Shíwǔ'),
    ChineseCharacter(16, '十六', 'Shíliù'),
    ChineseCharacter(17, '十七', 'Shíqī'),
    ChineseCharacter(18, '十八', 'Shíbā'),
    ChineseCharacter(19, '十九', 'Shíjiǔ'),
    ChineseCharacter(20, '二十', 'Èrshí'),
    ChineseCharacter(21, '二十一', 'Èrshíyī'),
    ChineseCharacter(22, '二十二', 'Èrshíèr'),
    ChineseCharacter(23, '二十三', 'Èrshísān'),
    ChineseCharacter(24, '二十四', 'Èrshísì'),
    ChineseCharacter(25, '二十五', 'Èrshíwǔ'),
    ChineseCharacter(26, '二十六', 'Èrshíliù'),
    ChineseCharacter(27, '二十七', 'Èrshíqī'),
    ChineseCharacter(28, '二十八', 'Èrshíbā'),
    ChineseCharacter(29, '二十九', 'Èrshíjiǔ'),
    ChineseCharacter(30, '三十', 'Sānshí'),
    ChineseCharacter(31, '三十一', 'Sānshíyī'),
    ChineseCharacter(32, '三十二', 'Sānshíèr'),
    ChineseCharacter(33, '三十三', 'Sānshísān'),
    ChineseCharacter(34, '三十四', 'Sānshísì'),
    ChineseCharacter(35, '三十五', 'Sānshíwǔ'),
    ChineseCharacter(36, '三十六', 'Sānshíliù'),
    ChineseCharacter(37, '三十七', 'Sānshíqī'),
    ChineseCharacter(38, '三十八', 'Sānshíbā'),
    ChineseCharacter(39, '三十九', 'Sānshíjiǔ'),
    ChineseCharacter(40, '四十', 'Sìshí'),
    ChineseCharacter(41, '四十一', 'Sìshíyī'),
    ChineseCharacter(42, '四十二', 'Sìshíèr'),
    ChineseCharacter(43, '四十三', 'Sìshísān'),
    ChineseCharacter(44, '四十四', 'Sìshísì'),
    ChineseCharacter(45, '四十五', 'Sìshíwǔ'),
    ChineseCharacter(46, '四十六', 'Sìshíliù'),
    ChineseCharacter(47, '四十七', 'Sìshíqī'),
    ChineseCharacter(48, '四十八', 'Sìshíbā'),
    ChineseCharacter(49, '四十九', 'Sìshíjiǔ'),
    ChineseCharacter(50, '五十', 'Wǔshí'),
    ChineseCharacter(51, '五十一', 'Wǔshíyī'),
    ChineseCharacter(52, '五十二', 'Wǔshíèr'),
    ChineseCharacter(53, '五十三', 'Wǔshísān'),
    ChineseCharacter(54, '五十四', 'Wǔshísì'),
    ChineseCharacter(55, '五十五', 'Wǔshíwǔ'),
    ChineseCharacter(56, '五十六', 'Wǔshíliù'),
    ChineseCharacter(57, '五十七', 'Wǔshíqī'),
    ChineseCharacter(58, '五十八', 'Wǔshíbā'),
    ChineseCharacter(59, '五十九', 'Wǔshíjiǔ'),
    ChineseCharacter(60, '六十', 'Liùshí'),
    ChineseCharacter(61, '六十一', 'Liùshíyī'),
    ChineseCharacter(62, '六十二', 'Liùshíèr'),
    ChineseCharacter(63, '六十三', 'Liùshísān'),
    ChineseCharacter(64, '六十四', 'Liùshísì'),
    ChineseCharacter(65, '六十五', 'Liùshíwǔ'),
    ChineseCharacter(66, '六十六', 'Liùshíliù'),
    ChineseCharacter(67, '六十七', 'Liùshíqī'),
    ChineseCharacter(68, '六十八', 'Liùshíbā'),
    ChineseCharacter(69, '六十九', 'Liùshíjiǔ'),
    ChineseCharacter(70, '七十', 'Qīshí'),
    ChineseCharacter(71, '七十一', 'Qīshíyī'),
    ChineseCharacter(72, '七十二', 'Qīshíèr'),
    ChineseCharacter(73, '七十三', 'Qīshísān'),
    ChineseCharacter(74, '七十四', 'Qīshísì'),
    ChineseCharacter(75, '七十五', 'Qīshíwǔ'),
    ChineseCharacter(76, '七十六', 'Qīshíliù'),
    ChineseCharacter(77, '七十七', 'Qīshíqī'),
    ChineseCharacter(78, '七十八', 'Qīshíbā'),
    ChineseCharacter(79, '七十九', 'Qīshíjiǔ'),
    ChineseCharacter(80, '八十', 'Bāshí'),
    ChineseCharacter(81, '八十一', 'Bāshíyī'),
    ChineseCharacter(82, '八十二', 'Bāshíèr'),
    ChineseCharacter(83, '八十三', 'Bāshísān'),
    ChineseCharacter(84, '八十四', 'Bāshísì'),
    ChineseCharacter(85, '八十五', 'Bāshíwǔ'),
    ChineseCharacter(86, '八十六', 'Bāshíliù'),
    ChineseCharacter(87, '八十七', 'Bāshíqī'),
    ChineseCharacter(88, '八十八', 'Bāshíbā'),
    ChineseCharacter(89, '八十九', 'Bāshíjiǔ'),
    ChineseCharacter(90, '九十', 'Jiǔshí'),
    ChineseCharacter(91, '九十一', 'Jiǔshíyī'),
    ChineseCharacter(92, '九十二', 'Jiǔshíèr'),
    ChineseCharacter(93, '九十三', 'Jiǔshísān'),
    ChineseCharacter(94, '九十四', 'Jiǔshísì'),
    ChineseCharacter(95, '九十五', 'Jiǔshíwǔ'),
    ChineseCharacter(96, '九十六', 'Jiǔshíliù'),
    ChineseCharacter(97, '九十七', 'Jiǔshíqī'),
    ChineseCharacter(98, '九十八', 'Jiǔshíbā'),
    ChineseCharacter(99, '九十九', 'Jiǔshíjiǔ'),
    ChineseCharacter(100, '一百', 'Yìbǎi'),
]

while True:
    current_character = random.choice(CHARACTERS)
    remaining_attempts = 2
    expected = as_ascii(current_character.pinyin.lower())

    while remaining_attempts > 0:
        answer = input(f"What does {current_character.character} mean? ")
        if answer.lower() == expected:
            print(current_character.pinyin)
            break
        else:
            print("Not quite!", end=" ")
            remaining_attempts -= 1
        if remaining_attempts == 0:
            print("Try this instead:")