import os
import json
from PIL import Image, ImageDraw
from IPython.display import display

# Directory and JSON filenames
datasets = [
    {"path": r"C:\dataset\Hard Hat Workers.v2-raw.coco\train", "json": "_annotations.coco.json"},
    {"path": r"C:\dataset\Hard Hat Workers.v2-raw.coco\test", "json": "_annotations.coco.json"},
    {"path": r"C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\val2017", "json": "instances_val217.json"},
    {"path": r"C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\test2017", "json": "instances_test2017.json"},
    {"path": r"C:\dataset\Hard Hat Workers.v2-raw.coco\V2\dataset\COCO\train2017", "json": "instances_train2017.json"}
]

# Category ID mapping
category_mapping = {
    1: "head",
    2: "helmet",
    3: "person"
}

# Initialize counters for each label
label_counts = {"head": 0, "helmet": 0, "person": 0}

# Function to generate thumbnail with annotations
def generate_thumbnail(image_path, annotations, category_mapping):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Draw bounding boxes
    for annotation in annotations:
        category_name = category_mapping.get(annotation['category_id'])
        bbox = annotation['bbox']
        draw.rectangle([bbox[0], bbox[1], bbox[0] + bbox[2], bbox[1] + bbox[3]], outline="red", width=2)
        draw.text((bbox[0], bbox[1]), category_name, fill="red")
    
    # Resize to thumbnail
    image.thumbnail((150, 150))
    
    return image

# Function to process each dataset
def process_dataset(dataset):
    json_path = os.path.join(dataset["path"], dataset["json"])
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    images_info = {img['id']: img for img in data['images']}
    
    # Dictionary to hold image annotations
    image_annotations = {img_id: [] for img_id in images_info.keys()}
    
    for ann in data['annotations']:
        image_annotations[ann['image_id']].append(ann)
        category_name = category_mapping.get(ann['category_id'])
        if category_name:
            label_counts[category_name] += 1
    
    # Generate report for each image
    report = []
    for img_id, annotations in image_annotations.items():
        image_info = images_info[img_id]
        image_path = os.path.join(dataset["path"], image_info['file_name'])
        thumbnail = generate_thumbnail(image_path, annotations, category_mapping)
        
        label_count_str = "<BR>".join([f"{category_mapping[ann['category_id']]}標籤數量: {len([a for a in annotations if a['category_id'] == ann['category_id']])}" for ann in annotations])
        report.append({
            "thumbnail": thumbnail,
            "label_count_str": label_count_str,
            "file_name": image_info['file_name']
        })
    
    return report

# Process each dataset and generate report
final_report = []
for dataset in datasets:
    final_report.extend(process_dataset(dataset))

# Display the report
for entry in final_report:
    display(entry['thumbnail'])
    print(f"{entry['label_count_str']} | {entry['file_name']}")

# Display summary counts
print("\nSummary:")
print(f"Head: {label_counts['head']}")
print(f"Helmet: {label_counts['helmet']}")
print(f"Person: {label_counts['person']}")
