#加密解密库hashlib
import hashlib

#md5加密
imooc = "imooc.com"
md5 = hashlib.md5()
md5.update(imooc.encode('utf-8'))
res = md5.hexdigest()
print(res)

#'dict' object has no attribute 'encode'字典类型不能加密需转为str
data = str({
    'key':'value'
})
md5.update(data.encode('utf-8'))
res1 = md5.hexdigest()
print(res1)