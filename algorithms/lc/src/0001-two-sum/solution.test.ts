import { twoSum } from "./solution";

describe("Two Sum", () => {
  test("should return indices of the two numbers that add up to the target", () => {
    expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
  });

  test("should handle another valid case", () => {
    expect(twoSum([3, 2, 4], 6)).toEqual([1, 2]);
  });

  test("should work with duplicate numbers", () => {
    expect(twoSum([3, 3], 6)).toEqual([0, 1]);
  });
});
