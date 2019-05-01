CREATE TABLE `logs` (
	`time` TIMESTAMP NOT NULL DEFAULT NOW() ON UPDATE CURRENT_TIMESTAMP,
	`relay1on` BOOLEAN DEFAULT false,
	`relay2on` BOOLEAN DEFAULT false,
	`soil1voltage` FLOAT,
	`soil2voltage` FLOAT,
	`soil3voltage` FLOAT,
	`soil4voltage` FLOAT,
	`soil5voltage` FLOAT,
	`soil6voltage` FLOAT,
	`soil7voltage` FLOAT,
	`soil8voltage` FLOAT,
	`humidity1` FLOAT,
	`humidity2` FLOAT,
	`temperature1` FLOAT,
	`temperature2` FLOAT,
	KEY `time_index` (`time`) USING BTREE
);