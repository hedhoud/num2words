# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words


class Num2WordsARTest(TestCase):

    def test_default_currency(self):
        self.assertEqual(num2words(1, to='currency', lang='tn'), 'واحد دينار')
        self.assertEqual(num2words(2, to='currency', lang='tn'), 'اثنان دينارين')
        self.assertEqual(num2words(10, to='currency', lang='tn'),'عشرا دينارات')
        self.assertEqual(num2words(100, to='currency', lang='tn'), 'مياة دينار')
        self.assertEqual(num2words(652.12, to='currency', lang='tn'),
                         'ستمياة و ثنين و خمسين دينار و أثناش فرنك')
        self.assertEqual(num2words(324, to='currency', lang='tn'),
                         'ثلاثميا و أربع و عشرين دينار')
        self.assertEqual(num2words(2000, to='currency', lang='tn'),
                         'ألفين دينار')
        self.assertEqual(num2words(541, to='currency', lang='tn'),
                         'خمسميا و واحد و أربعين دينار')
        self.assertEqual(num2words(10000, to='currency', lang='tn'),
                         'عشرا آلاف دينار')
        self.assertEqual(num2words(20000.12, to='currency', lang='tn'),
                         'عشرين ألف دينار و أثناش فرنك')
        self.assertEqual(num2words(1000000, to='currency', lang='tn'),
                         'مليون دينار')
        val = 'تسعميا و ثلاث و عشرين ألف و أربعميا و حداش دينار'
        self.assertEqual(num2words(923411, to='currency', lang='tn'), val)
        self.assertEqual(num2words(63411, to='currency', lang='tn'),
                         'ثلاث و ستين ألف و أربعميا و حداش دينار')
        self.assertEqual(num2words(1000000.99, to='currency', lang='tn'),
                         'مليون دينار و تسع و تسعين فرنك')

    def test_ordinal(self):

        self.assertEqual(num2words(1, to='ordinal', lang='tn'), 'اللول')
        self.assertEqual(num2words(2, to='ordinal', lang='tn'), 'ثاني')
        self.assertEqual(num2words(3, to='ordinal', lang='tn'), 'ثالث')
        self.assertEqual(num2words(4, to='ordinal', lang='tn'), 'رابع')
        self.assertEqual(num2words(5, to='ordinal', lang='tn'), 'خامس')
        self.assertEqual(num2words(6, to='ordinal', lang='tn'), 'سادس')
        self.assertEqual(num2words(9, to='ordinal', lang='tn'), 'تاسع')
        self.assertEqual(num2words(20, to='ordinal', lang='tn'), 'عشرين')
        self.assertEqual(num2words(94, to='ordinal', lang='tn'),
                         'أربع و تسعين')
        self.assertEqual(num2words(102, to='ordinal', lang='tn'),
                         'ميا و ثنين')
        self.assertEqual(
            num2words(923411, to='ordinal_num', lang='tn'),
            'تسعميا و ثلاث و عشرين ألف و أربعميا و حداش')

        # See https://github.com/savoirfairelinux/num2words/issues/403
        self.assertEqual(num2words(23, lang="tn"), 'ثلاث و عشرين')
        self.assertEqual(num2words(23, to='ordinal',
                         lang="tn"), 'ثلاث و عشرين')

    def test_cardinal(self):
        self.assertEqual(num2words(0, to='cardinal', lang='tn'), 'صفر')
        self.assertEqual(num2words(12, to='cardinal', lang='tn'), 'أثناش')
        self.assertEqual(num2words(12.3, to='cardinal', lang='tn'),
                         'أثناش  , ثلاثين')
        self.assertEqual(num2words(12.01, to='cardinal', lang='tn'),
                         'أثناش  , واحد')
        self.assertEqual(num2words(12.02, to='cardinal', lang='tn'),
                         'أثناش  , ثنين')
        self.assertEqual(num2words(12.03, to='cardinal', lang='tn'),
                         'أثناش  , ثلاث')
        self.assertEqual(num2words(12.34, to='cardinal', lang='tn'),
                         'أثناش  , أربع و ثلاثين')
        # Not implemented
        self.assertEqual(num2words(12.345, to='cardinal', lang='tn'),
                         num2words(12.34, to='cardinal', lang='tn'))
        self.assertEqual(num2words(-8324, to='cardinal', lang='tn'),
                         'سالب ثمانية آلاف و ثلاثمائة و أربعة و عشرون')

        self.assertEqual(num2words(200, to='cardinal', lang='tn'),
                         'ميتين')
        self.assertEqual(num2words(700, to='cardinal', lang='tn'),
                         'سبعميا')
        self.assertEqual(num2words(101010, to='cardinal', lang='tn'),
                         'ميا و ألف ألف و عشرا')

        self.assertEqual(
            num2words(3431.12, to='cardinal', lang='tn'),
            'ثلاث آلاف و أربعميا و واحد و ثلاثين  , أثناش')
        self.assertEqual(num2words(431, to='cardinal', lang='tn'),
                         'أربعميا و واحد و ثلاثين')
        self.assertEqual(num2words(94231, to='cardinal', lang='tn'),
                         'أربع و تسعين ألف و ميتين و واحد و ثلاثين')
        self.assertEqual(num2words(1431, to='cardinal', lang='tn'),
                         'ألف و أربعميا و واحد و ثلاثين')
        self.assertEqual(num2words(740, to='cardinal', lang='tn'),
                         'سبعميا و أربعين')
        self.assertEqual(num2words(741, to='cardinal', lang='tn'),
                         # 'سبعة مائة و واحد و أربعون'
                         'سبعميا و واحد و أربعين'
                         )
        self.assertEqual(num2words(262, to='cardinal', lang='tn'),
                         'ميتين و ثنين و ستين'
                         )
        self.assertEqual(num2words(798, to='cardinal', lang='tn'),
                         'سبعميا و ثمني و تسعين'
                         )
        self.assertEqual(num2words(710, to='cardinal', lang='tn'),
                         'سبعميا و عشرا')
        self.assertEqual(num2words(711, to='cardinal', lang='tn'),
                         # 'سبعة مائة و إحدى عشر'
                         'سبعميا و حداش'
                         )
        self.assertEqual(num2words(700, to='cardinal', lang='tn'),
                         'سبعميا')
        self.assertEqual(num2words(701, to='cardinal', lang='tn'),
                         'سبعميا و واحد')

        self.assertEqual(
            num2words(1258888, to='cardinal', lang='tn'),
            'مليون و ميتين و ثمني و خمسين ألف و ثمانميا و ثمني و ثمانين'
        )

        self.assertEqual(num2words(1100, to='cardinal', lang='tn'),
                         'ألف و ميا')

        self.assertEqual(num2words(1000000521, to='cardinal', lang='tn'),
                         'مليار و خمسميا و واحد و عشرين')

    def test_prefix_and_suffix(self):
        self.assertEqual(num2words(645, to='currency',
                                   lang='tn', prefix="فقط", suffix="لاغير"),
                         'فقط ستميا و خمس و أربعين دينار لاغير')

    def test_year(self):
        self.assertEqual(num2words(2000, to='year', lang='tn'), 'ألفين')

    def test_max_numbers(self):

        for number in 10**51, 10**51 + 2:

            with self.assertRaises(OverflowError) as context:
                num2words(number, lang='tn')

            self.assertTrue('must be less' in str(context.exception))

    def test_big_numbers(self):
        self.assertEqual(
            num2words(1000000045000000000000003000000002000000300,
                      to='cardinal', lang='tn'),
            'تريديسيليون و خمس و أربعين ديسيليون و ثلاث كوينتليونات و ملييرين و ثلاثميا'
        )
        self.assertEqual(
            num2words(-1000000000000000000000003000000002000000302,
                      to='cardinal', lang='tn'),
            'سالب تريديسيليون و ثلاث كوينتليونات و ملييرين و ثلاثميا و ثنين'
        )
        self.assertEqual(
            num2words(9999999999999999999999999999999999999999999999992,
                      to='cardinal', lang='tn'),
                'تسع كوينتينيليونات و تسعميا و تسع و تسعين كوادريسيليون و تسعميا و تسع و تسعين تريديسيليون و تسعميا \
                و تسع و تسعين دوديسيليون و تسعميا و تسع و تسعين أندسيليون و تسعميا و تسع و تسعين ديسيليون و تسعميا\
                و تسع و تسعين نونيليون و تسعميا و تسع و تسعين أوكتيليون و تسعميا\
                و تسع و تسعين سبتيليون و تسعميا و تسع و تسعين سكستيليون و تسعميا و تسع و تسعين كوينتليون\
                و تسعميا و تسع و تسعين كوادريليون و تسعميا و تسع و تسعين تريليون و تسعميا\
                و تسع و تسعين مليار و تسعميا و تسع و تسعين مليون و تسعميا و تسع و تسعين ألف و تسعميا و ثنين و تسعين'
        )
