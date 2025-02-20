# Copyright 2025 Webullpay
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

######################## BEGIN LICENSE BLOCK ########################
# The Original Code is Mozilla Communicator client code.
#
# The Initial Developer of the Original Code is
# Netscape Communications Corporation.
# Portions created by the Initial Developer are Copyright (C) 1998
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Mark Pilgrim - port to Python
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
# 02110-1301  USA
######################### END LICENSE BLOCK #########################

# 255: Control characters that usually does not exist in any text
# 254: Carriage/Return
# 253: symbol (punctuation) that does not belong to word
# 252: 0 - 9

# The following result for thai was collected from a limited sample (1M).

# Character Mapping Table:
TIS620CharToOrderMap = (
255,255,255,255,255,255,255,255,255,255,254,255,255,254,255,255,  # 00
255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,  # 10
253,253,253,253,253,253,253,253,253,253,253,253,253,253,253,253,  # 20
252,252,252,252,252,252,252,252,252,252,253,253,253,253,253,253,  # 30
253,182,106,107,100,183,184,185,101, 94,186,187,108,109,110,111,  # 40
188,189,190, 89, 95,112,113,191,192,193,194,253,253,253,253,253,  # 50
253, 64, 72, 73,114, 74,115,116,102, 81,201,117, 90,103, 78, 82,  # 60
 96,202, 91, 79, 84,104,105, 97, 98, 92,203,253,253,253,253,253,  # 70
209,210,211,212,213, 88,214,215,216,217,218,219,220,118,221,222,
223,224, 99, 85, 83,225,226,227,228,229,230,231,232,233,234,235,
236,  5, 30,237, 24,238, 75,  8, 26, 52, 34, 51,119, 47, 58, 57,
 49, 53, 55, 43, 20, 19, 44, 14, 48,  3, 17, 25, 39, 62, 31, 54,
 45,  9, 16,  2, 61, 15,239, 12, 42, 46, 18, 21, 76,  4, 66, 63,
 22, 10,  1, 36, 23, 13, 40, 27, 32, 35, 86,240,241,242,243,244,
 11, 28, 41, 29, 33,245, 50, 37,  6,  7, 67, 77, 38, 93,246,247,
 68, 56, 59, 65, 69, 60, 70, 80, 71, 87,248,249,250,251,252,253,
)

# Model Table:
# total sequences: 100%
# first 512 sequences: 92.6386%
# first 1024 sequences:7.3177%
# rest  sequences:     1.0230%
# negative sequences:  0.0436%
ThaiLangModel = (
0,1,3,3,3,3,0,0,3,3,0,3,3,0,3,3,3,3,3,3,3,3,0,0,3,3,3,0,3,3,3,3,
0,3,3,0,0,0,1,3,0,3,3,2,3,3,0,1,2,3,3,3,3,0,2,0,2,0,0,3,2,1,2,2,
3,0,3,3,2,3,0,0,3,3,0,3,3,0,3,3,3,3,3,3,3,3,3,0,3,2,3,0,2,2,2,3,
0,2,3,0,0,0,0,1,0,1,2,3,1,1,3,2,2,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,
3,3,3,2,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,3,3,2,3,2,3,3,2,2,2,
3,1,2,3,0,3,3,2,2,1,2,3,3,1,2,0,1,3,0,1,0,0,1,0,0,0,0,0,0,0,1,1,
3,3,2,2,3,3,3,3,1,2,3,3,3,3,3,2,2,2,2,3,3,2,2,3,3,2,2,3,2,3,2,2,
3,3,1,2,3,1,2,2,3,3,1,0,2,1,0,0,3,1,2,1,0,0,1,0,0,0,0,0,0,1,0,1,
3,3,3,3,3,3,2,2,3,3,3,3,2,3,2,2,3,3,2,2,3,2,2,2,2,1,1,3,1,2,1,1,
3,2,1,0,2,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,
3,3,3,2,3,2,3,3,2,2,3,2,3,3,2,3,1,1,2,3,2,2,2,3,2,2,2,2,2,1,2,1,
2,2,1,1,3,3,2,1,0,1,2,2,0,1,3,0,0,0,1,1,0,0,0,0,0,2,3,0,0,2,1,1,
3,3,2,3,3,2,0,0,3,3,0,3,3,0,2,2,3,1,2,2,1,1,1,0,2,2,2,0,2,2,1,1,
0,2,1,0,2,0,0,2,0,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,
3,3,2,3,3,2,0,0,3,3,0,2,3,0,2,1,2,2,2,2,1,2,0,0,2,2,2,0,2,2,1,1,
0,2,1,0,2,0,0,2,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,
3,3,2,3,2,3,2,0,2,2,1,3,2,1,3,2,1,2,3,2,2,3,0,2,3,2,2,1,2,2,2,2,
1,2,2,0,0,0,0,2,0,1,2,0,1,1,1,0,1,0,3,1,1,0,0,0,0,0,0,0,0,0,1,0,
3,3,2,3,3,2,3,2,2,2,3,2,2,3,2,2,1,2,3,2,2,3,1,3,2,2,2,3,2,2,2,3,
3,2,1,3,0,1,1,1,0,2,1,1,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,2,0,0,
1,0,0,3,0,3,3,3,3,3,0,0,3,0,2,2,3,3,3,3,3,0,0,0,1,1,3,0,0,0,0,2,
0,0,1,0,0,0,0,0,0,0,2,3,0,0,0,3,0,2,0,0,0,0,0,3,0,0,0,0,0,0,0,0,
2,0,3,3,3,3,0,0,2,3,0,0,3,0,3,3,2,3,3,3,3,3,0,0,3,3,3,0,0,0,3,3,
0,0,3,0,0,0,0,2,0,0,2,1,1,3,0,0,1,0,0,2,3,0,1,0,0,0,0,0,0,0,1,0,
3,3,3,3,2,3,3,3,3,3,3,3,1,2,1,3,3,2,2,1,2,2,2,3,1,1,2,0,2,1,2,1,
2,2,1,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,
3,0,2,1,2,3,3,3,0,2,0,2,2,0,2,1,3,2,2,1,2,1,0,0,2,2,1,0,2,1,2,2,
0,1,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,3,3,2,1,3,3,1,1,3,0,2,3,1,1,3,2,1,1,2,0,2,2,3,2,1,1,1,1,1,2,
3,0,0,1,3,1,2,1,2,0,3,0,0,0,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,
3,3,1,1,3,2,3,3,3,1,3,2,1,3,2,1,3,2,2,2,2,1,3,3,1,2,1,3,1,2,3,0,
2,1,1,3,2,2,2,1,2,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
3,3,2,3,2,3,3,2,3,2,3,2,3,3,2,1,0,3,2,2,2,1,2,2,2,1,2,2,1,2,1,1,
2,2,2,3,0,1,3,1,1,1,1,0,1,1,0,2,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,3,3,2,3,2,2,1,1,3,2,3,2,3,2,0,3,2,2,1,2,0,2,2,2,1,2,2,2,2,1,
3,2,1,2,2,1,0,2,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,
3,3,3,3,3,2,3,1,2,3,3,2,2,3,0,1,1,2,0,3,3,2,2,3,0,1,1,3,0,0,0,0,
3,1,0,3,3,0,2,0,2,1,0,0,3,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,3,2,3,2,3,3,0,1,3,1,1,2,1,2,1,1,3,1,1,0,2,3,1,1,1,1,1,1,1,1,
3,1,1,2,2,2,2,1,1,1,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
3,2,2,1,1,2,1,3,3,2,3,2,2,3,2,2,3,1,2,2,1,2,0,3,2,1,2,2,2,2,2,1,
3,2,1,2,2,2,1,1,1,1,0,0,1,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,3,3,3,3,3,3,1,3,3,0,2,1,0,3,2,0,0,3,1,0,1,1,0,1,0,0,0,0,0,1,
1,0,0,1,0,3,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,2,2,2,3,0,0,1,3,0,3,2,0,3,2,2,3,3,3,3,3,1,0,2,2,2,0,2,2,1,2,
0,2,3,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
3,0,2,3,1,3,3,2,3,3,0,3,3,0,3,2,2,3,2,3,3,3,0,0,2,2,3,0,1,1,1,3,
0,0,3,0,0,0,2,2,0,1,3,0,1,2,2,2,3,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,
3,2,3,3,2,0,3,3,2,2,3,1,3,2,1,3,2,0,1,2,2,0,2,3,2,1,0,3,0,0,0,0,
3,0,0,2,3,1,3,0,0,3,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,1,3,2,2,2,1,2,0,1,3,1,1,3,1,3,0,0,2,1,1,1,1,2,1,1,1,0,2,1,0,1,
1,2,0,0,0,3,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,3,1,0,0,0,1,0,
3,3,3,3,2,2,2,2,2,1,3,1,1,1,2,0,1,1,2,1,2,1,3,2,0,0,3,1,1,1,1,1,
3,1,0,2,3,0,0,0,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,2,3,0,3,3,0,2,0,0,0,0,0,0,0,3,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,2,3,1,3,0,0,1,2,0,0,2,0,3,3,2,3,3,3,2,3,0,0,2,2,2,0,0,0,2,2,
0,0,1,0,0,0,0,3,0,0,0,0,2,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,
0,0,0,3,0,2,0,0,0,0,0,0,0,0,0,0,1,2,3,1,3,3,0,0,1,0,3,0,0,0,0,0,
0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,1,2,3,1,2,3,1,0,3,0,2,2,1,0,2,1,1,2,0,1,0,0,1,1,1,1,0,1,0,0,
1,0,0,0,0,1,1,0,3,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,3,3,2,1,0,1,1,1,3,1,2,2,2,2,2,2,1,1,1,1,0,3,1,0,1,3,1,1,1,1,
1,1,0,2,0,1,3,1,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,1,
3,0,2,2,1,3,3,2,3,3,0,1,1,0,2,2,1,2,1,3,3,1,0,0,3,2,0,0,0,0,2,1,
0,1,0,0,0,0,1,2,0,1,1,3,1,1,2,2,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,
0,0,3,0,0,1,0,0,0,3,0,0,3,0,3,1,0,1,1,1,3,2,0,0,0,3,0,0,0,0,2,0,
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,
3,3,1,3,2,1,3,3,1,2,2,0,1,2,1,0,1,2,0,0,0,0,0,3,0,0,0,3,0,0,0,0,
3,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,1,2,0,3,3,3,2,2,0,1,1,0,1,3,0,0,0,2,2,0,0,0,0,3,1,0,1,0,0,0,
0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,2,3,1,2,0,0,2,1,0,3,1,0,1,2,0,1,1,1,1,3,0,0,3,1,1,0,2,2,1,1,
0,2,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,0,3,1,2,0,0,2,2,0,1,2,0,1,0,1,3,1,2,1,0,0,0,2,0,3,0,0,0,1,0,
0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,1,1,2,2,0,0,0,2,0,2,1,0,1,1,0,1,1,1,2,1,0,0,1,1,1,0,2,1,1,1,
0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,
0,0,0,2,0,1,3,1,1,1,1,0,0,0,0,3,2,0,1,0,0,0,1,2,0,0,0,1,0,0,0,0,
0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,3,3,3,3,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
1,0,2,3,2,2,0,0,0,1,0,0,0,0,2,3,2,1,2,2,3,0,0,0,2,3,1,0,0,0,1,1,
0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,
3,3,2,2,0,1,0,0,0,0,2,0,2,0,1,0,0,0,1,1,0,0,0,2,1,0,1,0,1,1,0,0,
0,1,0,2,0,0,1,0,3,0,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,1,0,0,1,0,0,0,0,0,1,1,2,0,0,0,0,1,0,0,1,3,1,0,0,0,0,1,1,0,0,
0,1,0,0,0,0,3,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,
3,3,1,1,1,1,2,3,0,0,2,1,1,1,1,1,0,2,1,1,0,0,0,2,1,0,1,2,1,1,0,1,
2,1,0,3,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
1,3,1,0,0,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,
0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,3,2,0,0,0,0,0,0,1,2,1,0,1,1,0,2,0,0,1,0,0,2,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,2,0,0,0,1,3,0,1,0,0,0,2,0,0,0,0,0,0,0,1,2,0,0,0,0,0,
3,3,0,0,1,1,2,0,0,1,2,1,0,1,1,1,0,1,1,0,0,2,1,1,0,1,0,0,1,1,1,0,
0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,2,2,1,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,
2,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,3,0,0,1,1,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
1,1,0,1,2,0,1,2,0,0,1,1,0,2,0,1,0,0,1,0,0,0,0,1,0,0,0,2,0,0,0,0,
1,0,0,1,0,1,1,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,2,1,3,0,0,0,0,1,1,0,0,0,0,0,0,0,3,
1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,0,1,0,1,0,0,2,0,0,2,0,0,1,1,2,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,
1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,
1,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,1,0,0,0,
2,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,3,0,0,0,
2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,1,0,0,0,0,
1,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,1,1,0,0,2,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
)

TIS620ThaiModel = {
  'char_to_order_map': TIS620CharToOrderMap,
  'precedence_matrix': ThaiLangModel,
  'typical_positive_ratio': 0.926386,
  'keep_english_letter': False,
  'charset_name': "TIS-620",
  'language': 'Thai',
}
