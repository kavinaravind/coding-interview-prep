import { mergeTwoLists } from "./solution";
import { arrayToList, listToArray } from "../utils/list-node";

describe("Merge Two Sorted Lists", () => {
  test("should merge two non-empty lists", () => {
    const list1 = arrayToList([1, 2, 4]);
    const list2 = arrayToList([1, 3, 4]);
    const merged = mergeTwoLists(list1, list2);
    expect(listToArray(merged)).toEqual([1, 1, 2, 3, 4, 4]);
  });

  test("should return an empty list when both lists are empty", () => {
    expect(listToArray(mergeTwoLists(null, null))).toEqual([]);
  });

  test("should return the second list when the first list is empty", () => {
    const list2 = arrayToList([0]);
    const merged = mergeTwoLists(null, list2);
    expect(listToArray(merged)).toEqual([0]);
  });
});
