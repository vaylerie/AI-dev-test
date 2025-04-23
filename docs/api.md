## 1. Upload Image (/upload)
Endpoint ini berfungsi untuk mengunggah embedding gambar ke dalam FAISS index menggunakan CLIP dan menyimpan data gambar (filename dan path) ke dalam database
- Method POST
- Form Data: image (png, jpg)

### Response Body Success: 200 OK

```json 
{
    "data": {
        "filepath": "static/image/aaaaa.jpg"
    }
}
```

### Response Body Failed: 400

```json 
{
    "data": "Failed to upload image"
}
```
___

## 2. Search Image (/search)
Endpoint ini berfungsi untuk mencari gambar yang paling mirip dengan membandingkan embedding gambar dalam FAISS index dengan embedding gambar baru
- Method POST
- Form Data: image (png, jpg)

### Response Body Success: 200 OK

```json 
{
    "data": [
        {
            "id": 11,
            "filename": "asdfghjkl.jpg",
            "confidence": 1.0
        },
        {
            "id": 444,
            "filename": "qwertyuiop.jpg",
            "confidence": 0.2629
        },
        {
            "id": 333,
            "filename": "zxcvbnm.jpg",
            "confidence": 0.0553
        }
    ]
}
```

### Response Body Failed: 400

```json 
{
    "data": "Failed to upload image"
}
```