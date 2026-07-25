#this is not using binary search.
def search(nums1, nums2):
    merged = sorted(nums1 + nums2)
    mid = len(merged) // 2
    if len(merged) % 2 == 0:
        x = (merged[mid] + merged[mid - 1]) / 2
    else:
        x = merged[mid]
    return x

nums1 = [1,3]
nums2 = [2]
print(search(nums1, nums2))