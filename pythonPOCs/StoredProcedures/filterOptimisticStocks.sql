CREATE DEFINER=`root`@`localhost` PROCEDURE `filterOptimisticStocks`()
BEGIN
SELECT count(*) FROM pyspark.walmart_stock where Open<Close; 
SELECT count(*) FROM pyspark.walmart_stock where Open>Close;
SELECT count(*) FROM pyspark.walmart_stock; 
SELECT count(*) FROM pyspark.walmart_stock where Open=Close;
END