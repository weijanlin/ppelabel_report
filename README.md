# ppelabel_report
標註資料報告範例
## GPT prompt 說明
### step 1
幫我用python 寫一個標註清單提供驗收, 清單格式如下, 圖片和 JSON 檔案以下有範例說明
|相片縮圖並畫上標註資訊|Head標籤數量 <BR> Helmet標籤數量 <BR> person標籤數量|相片名稱|
|----------|-------------------------------|---------------------------|

圖片和 JSON 檔案的路徑已更新至 C:\dataset\Hard Hat Workers.v2-raw.coco\train，並且 JSON 檔名為 _annotations.coco.json , json 檔案格式如下:
```
{
    "info": {
        "year": "2020",
        "version": "2",
        "description": "Exported from roboflow.ai",
        "contributor": "Northeastern University - China",
        "url": "https://public.roboflow.ai/object-detection/hard-hat-workers",
        "date_created": "2020-04-30T03:26:22+00:00"
    },
    "licenses": [
        {
            "id": 1,
            "url": "https://creativecommons.org/publicdomain/zero/1.0/",
            "name": "Public Domain"
        }
    ],
    "categories": [
        {
            "id": 0,
            "name": "Workers",
            "supercategory": "none"
        },
        {
            "id": 1,
            "name": "head",
            "supercategory": "Workers"
        },
        {
            "id": 2,
            "name": "helmet",
            "supercategory": "Workers"
        },
        {
            "id": 3,
            "name": "person",
            "supercategory": "Workers"
        }
    ],
    "images": [
        {
            "id": 0,
            "license": 1,
            "file_name": "002310_jpg.rf.0008cd4590d2edb0e1447329236d9c11.jpg",
            "height": 319,
            "width": 489,
            "date_captured": "2020-04-30T03:26:22+00:00"
        },
        {
            "id": 1,
            "license": 1,
            "file_name": "003626_jpg.rf.0024e8fc3c8c3f411962ca8dab7b8e92.jpg",
            "height": 384,
            "width": 500,
            "date_captured": "2020-04-30T03:26:22+00:00"
        }
    ],
    "annotations": [
        {
            "image_id": 0,
            "category_id": 2,
            "bbox": [50, 60, 100, 200]
        },
        {
            "image_id": 1,
            "category_id": 3,
            "bbox": [30, 40, 120, 180]
        }
    ]
}
```
### step 2
太棒了, 但目前有5個目錄要合併作報告, 最後結尾要有一個統計, head, helmet ,person 標籤各有幾個, 目錄及json 名稱如下
圖片和 JSON 檔案的路徑已更新至 C:\dataset\Hard Hat Workers.v2-raw.coco\train，並且 JSON 檔名為 _annotations.coco.json
及 
圖片和 JSON 檔案的路徑已更新至 C:\dataset\Hard Hat Workers.v2-raw.coco\test ，並且 JSON 檔名為 _annotations.coco.json
圖片和 JSON 檔案的路徑已更新至 C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\val2017
JSON 檔名為instances_val217.json 
圖片和 JSON 檔案的路徑已更新至 C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\test2017
JSON 檔名為instances_test2017.json
圖片和 JSON 檔案的路徑已更新至C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\train2017
JSON 檔名為instances_train2017.json
