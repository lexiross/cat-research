const fs       = require("fs");
const _        = require("lodash");
const parseCSV = require("csv-parse/lib/sync");
const stringifyCSV = require("csv-stringify/lib/sync");

const IN_FILE = "./data-raw.csv"
const OUT_FILE = "./data-clean.csv"

const SIZE_MAP = {
  "smol": 0,
  "Medium": 1,
  "Lorge": 2,
  "THICC": 3,
};
const SEX_MAP = {
  "Male": -1,
  "Other": 0,
  "Female": 1,
};
const AGE_MAP = {
  "0-6 months": 0,
  "6-12 months": 0,
  "1-2 years": 1,
  "2-5 years": 2,
  "5-10 years": 3,
  "10+ years": 4,
};
const OUTDOORNESS_MAP = {
  "Indoors": 0,
  "Indoors only": 0,
  "Indoors + backyard": 1,
  "Indoors + roams free outdoors": 2,
  "Outdoors only": 3,
};
const FUR_MAP = {
  "None (e.g. sphinx cat)": 0,
  "Short": 1,
  "Long": 2,
};


const rawDataString = fs.readFileSync(IN_FILE).toString();
const rawRows = parseCSV(rawDataString);

const transformedRows = rawRows.slice(1).map((row) => {
  const [_, __, behaviorsRaw, size, sex, age, outdoorness, fur] = row;
  const result = {};

  result.size = SIZE_MAP[size];
  result.sex = SEX_MAP[sex];
  result.age = AGE_MAP[age];
  result.outdoorness = OUTDOORNESS_MAP[outdoorness];
  result.fur = FUR_MAP[fur];

  const behaviors = behaviorsRaw.toLowerCase();

  const hasBehavior = (behavior) => Number(behaviors.includes(behavior));

  result.paws_door = hasBehavior("paws at");
  result.muffins = hasBehavior("kneads");
  result.belly_trap = hasBehavior("belly rub");
  result.corners = hasBehavior("on corners");
  result.boxes = hasBehavior("boxes");
  result.contort = hasBehavior("contorted");
  result.drools = hasBehavior("drools");
  result.sprints = hasBehavior("sprints");
  result.veggie = hasBehavior("non-meat");
  result.sheets = hasBehavior("under sheets");
  result.men = hasBehavior("prefers men");
  result.toes = hasBehavior("attacks toes");
  result.knocks = hasBehavior("knocks things");
  result.keyboard = hasBehavior("keyboards");
  result.stares = hasBehavior("stares intensely");
  result.blep = hasBehavior("blep");
  result.faucet = hasBehavior("faucet");
  result.food_freak = hasBehavior("freaks out");
  result.hind_legs = hasBehavior("hind legs");

  return result;
});

const outputCSV = stringifyCSV(transformedRows, {header: true});

fs.writeFileSync(OUT_FILE, outputCSV);

// console.log(_.countBy(transformedRows, "size"));
// console.log(_.countBy(transformedRows, "sex"));
// console.log(_.countBy(transformedRows, "age"));
// console.log(_.countBy(transformedRows, "outdoorness"));
// console.log(_.countBy(transformedRows, "fur"));
// console.log(_.countBy(transformedRows, "paws_door"));

// console.log(transformedRows.slice(0, 10))

