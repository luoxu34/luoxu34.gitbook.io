# Common Python Usages

## 漂亮的json格式

```python
import json
data = dict(name='广州', area_code='020')
print(json.dumps(data, indent=4, ensure_ascii=False))
```

Output:
```json
{
    "name": "广州",
    "area_code": "020"
}
```

